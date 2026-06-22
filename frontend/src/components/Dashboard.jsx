export default function Dashboard({ run }) {
  if (!run) {
    return (
      <section className="panel">
        <h3>Latest Run</h3>
        <p>No interpolation run yet. Upload at least two satellite files to begin.</p>
      </section>
    );
  }

  return (
    <section className="panel" id="pipeline">
      <div className="panel-heading">
        <h3>Latest Run</h3>
        <span>{run.status.toUpperCase()}</span>
      </div>
      <p>
        Satellite: <strong>{run.satellite_source || "Unknown"}</strong>
      </p>
      <p>
        Source files: <strong>{run.source_files.join(", ")}</strong>
      </p>
      <p>
        Generated frames: <strong>{run.output_frames.join(", ")}</strong>
      </p>
      <p className="muted">Generated at {new Date(run.created_at).toLocaleString()}</p>
    </section>
  );
}
