import { getArtifactUrl } from "../services/api";

export default function ResultsViewer({ run }) {
  const previewImage = run?.preview_images?.[0];

  return (
    <section className="panel">
      <div className="panel-heading">
        <h3>Generated Frames</h3>
        <span>{run ? run.output_frames.length : 0} frames</span>
      </div>
      {!run ? (
        <p className="muted">Frame previews appear here after a demo run.</p>
      ) : (
        <div className="frames-grid">
          <article className="frame-card">
            <h4>{run.output_frames[0]}</h4>
            {previewImage ? (
              <img
                className="result-image"
                src={getArtifactUrl(previewImage)}
                alt="Generated interpolated frame preview"
              />
            ) : (
              <p className="muted">No preview image available.</p>
            )}
            <p>{run.message}</p>
          </article>
        </div>
      )}
    </section>
  );
}
