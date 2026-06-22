import { SATELLITE_OPTIONS } from "../utils/constants";

export default function DataUpload({
  satellite,
  onSatelliteChange,
  onRun,
  onUpload,
  onFilesChange,
  selectedFiles,
  uploadedFiles,
  isUploading,
  isInterpolating,
}) {
  const availableFileCount = Math.max(selectedFiles.length, uploadedFiles.length);

  return (
    <section className="panel" id="overview">
      <div className="panel-heading">
        <h3>Satellite Input</h3>
        <span>Live backend workflow</span>
      </div>
      <label className="field">
        <span>Satellite source</span>
        <select
          id="satellite-source"
          name="satellite_source"
          value={satellite}
          onChange={(event) => onSatelliteChange(event.target.value)}
        >
          {SATELLITE_OPTIONS.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
      </label>
      <label className="field">
        <span>Satellite files (.nc, .h5)</span>
        <input
          id="satellite-files"
          name="satellite_files"
          type="file"
          accept=".nc,.h5"
          multiple
          onChange={onFilesChange}
        />
      </label>
      <p className="muted">
        Selected: {selectedFiles.length ? selectedFiles.map((file) => file.name).join(", ") : "No files selected"}
      </p>
      <div className="action-row">
        <button
          className="primary-button"
          onClick={onUpload}
          disabled={(isUploading || isInterpolating) || selectedFiles.length < 1}
        >
          {isUploading ? "Uploading..." : "Upload Files"}
        </button>
        <button
          className="secondary-button"
          onClick={onRun}
          disabled={(isUploading || isInterpolating) || availableFileCount < 2}
        >
          {isInterpolating ? "Interpolating..." : "Run Interpolation"}
        </button>
      </div>
      <p className="muted">Interpolation ke liye kam se kam 2 files chahiye.</p>
      <div className="uploaded-files">
        <h4>Uploaded Files</h4>
        {uploadedFiles.length === 0 ? (
          <p className="muted">No uploaded files yet.</p>
        ) : (
          uploadedFiles.map((file) => (
            <div key={file.filename} className="uploaded-file-row">
              <span>{file.filename}</span>
              <span>{file.size_bytes} bytes</span>
            </div>
          ))
        )}
      </div>
    </section>
  );
}
