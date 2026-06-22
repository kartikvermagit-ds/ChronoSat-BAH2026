from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

try:
    import h5py
except ImportError:  # pragma: no cover
    h5py = None

try:
    import xarray as xr
except ImportError:  # pragma: no cover
    xr = None


@dataclass(slots=True)
class SatelliteFrame:
    filename: str
    file_path: Path
    file_type: str
    band_name: str
    array: np.ndarray


class SatelliteDataReader:
    def read(self, file_path: Path) -> SatelliteFrame:
        suffix = file_path.suffix.lower()
        if suffix == ".nc":
            return self._read_netcdf(file_path)
        if suffix == ".h5":
            return self._read_hdf5(file_path)
        raise ValueError(f"Unsupported satellite file type: {file_path.suffix}")

    def _read_netcdf(self, file_path: Path) -> SatelliteFrame:
        if xr is None:
            return self._fallback_frame(file_path, "fallback_netcdf")
        try:
            dataset = xr.open_dataset(file_path)
            for variable_name, data_array in dataset.data_vars.items():
                candidate = self._to_2d_array(data_array.values)
                if candidate is not None:
                    return SatelliteFrame(
                        filename=file_path.name,
                        file_path=file_path,
                        file_type="netcdf",
                        band_name=variable_name,
                        array=candidate,
                    )
        except Exception:
            return self._fallback_frame(file_path, "fallback_netcdf")
        return self._fallback_frame(file_path, "fallback_netcdf")

    def _read_hdf5(self, file_path: Path) -> SatelliteFrame:
        if h5py is None:
            return self._fallback_frame(file_path, "fallback_hdf5")
        try:
            with h5py.File(file_path, "r") as handle:
                dataset_name, array = self._first_2d_dataset(handle)
                if array is not None:
                    return SatelliteFrame(
                        filename=file_path.name,
                        file_path=file_path,
                        file_type="hdf5",
                        band_name=dataset_name,
                        array=array,
                    )
        except Exception:
            return self._fallback_frame(file_path, "fallback_hdf5")
        return self._fallback_frame(file_path, "fallback_hdf5")

    def _first_2d_dataset(self, group, prefix: str = "") -> tuple[str, np.ndarray | None]:
        for key, value in group.items():
            current_name = f"{prefix}/{key}" if prefix else key
            if hasattr(value, "shape") and value.shape:
                candidate = self._to_2d_array(np.asarray(value))
                if candidate is not None:
                    return current_name, candidate
            if hasattr(value, "items"):
                nested_name, nested_array = self._first_2d_dataset(value, current_name)
                if nested_array is not None:
                    return nested_name, nested_array
        return prefix or "unknown", None

    def _to_2d_array(self, values: np.ndarray) -> np.ndarray | None:
        array = np.asarray(values)
        if array.ndim < 2:
            return None
        squeezed = np.squeeze(array)
        if squeezed.ndim == 2:
            return squeezed.astype(np.float32)
        if squeezed.ndim > 2:
            return squeezed[0].astype(np.float32)
        return None

    def _fallback_frame(self, file_path: Path, band_name: str) -> SatelliteFrame:
        raw = file_path.read_bytes()
        if not raw:
            raw = b"\x00" * 256
        values = np.frombuffer(raw, dtype=np.uint8).astype(np.float32)
        side = max(16, int(np.sqrt(values.size)))
        padded = np.pad(values, (0, max(0, side * side - values.size)), mode="wrap")
        array = padded[: side * side].reshape(side, side)
        return SatelliteFrame(
            filename=file_path.name,
            file_path=file_path,
            file_type=file_path.suffix.lower().lstrip("."),
            band_name=band_name,
            array=array,
        )
