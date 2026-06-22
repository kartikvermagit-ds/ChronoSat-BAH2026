import {
  listResults,
  listUploadedFiles,
  startInterpolation,
  uploadSatelliteFiles,
} from "./api";

export async function fetchUploadedFiles() {
  return listUploadedFiles();
}

export async function uploadFilesOnly(files) {
  return uploadSatelliteFiles(files);
}

export async function runInterpolationOnly({ sourceFiles, satellite }) {
  const interpolationResponse = await startInterpolation({
    source_files: sourceFiles.slice(0, 2),
    output_format: "png",
    satellite_source: satellite,
  });
  const resultsResponse = await listResults();

  return {
    run: interpolationResponse,
    results: resultsResponse,
  };
}

export async function executeProcessingFlow({ files, satellite }) {
  const uploadResponse = await uploadSatelliteFiles(files);
  const sourceFiles = uploadResponse.files.map((file) => file.filename);
  const interpolationResponse = await startInterpolation({
    source_files: sourceFiles.slice(0, 2),
    output_format: "png",
    satellite_source: satellite,
  });
  const resultsResponse = await listResults();

  return {
    upload: uploadResponse,
    run: interpolationResponse,
    results: resultsResponse,
  };
}
