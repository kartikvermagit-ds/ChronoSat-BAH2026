import { useMemo, useState } from "react";

import { getArtifactUrl } from "../services/api";
import logo from "../logo.png";

export default function BeforeAfterDemo({ run, uploadedFiles }) {
  const [position, setPosition] = useState(52);
  const groundTruthImage = useMemo(() => {
    const firstPreview = uploadedFiles?.[0]?.preview_image;
    return firstPreview ? getArtifactUrl(firstPreview) : logo;
  }, [uploadedFiles]);
  const interpolatedImage = useMemo(() => {
    const preview = run?.preview_images?.[0];
    return preview ? getArtifactUrl(preview) : logo;
  }, [run]);

  return (
    <section className="panel comparison-panel" id="comparison">
      <div className="panel-heading">
        <h3>Before vs After Demo</h3>
        <span>Ground truth cloud frame vs interpolated cloud frame</span>
      </div>
      <div className="comparison-stage">
        <img className="comparison-image base" src={groundTruthImage} alt="Ground truth cloud frame" />
        <div className="comparison-overlay" style={{ width: `${position}%` }}>
          <img
            className="comparison-image overlay"
            src={interpolatedImage}
            alt="Interpolated cloud frame"
          />
        </div>
        <div className="comparison-divider" style={{ left: `${position}%` }} />
        <div className="comparison-label ground">Ground Truth</div>
        <div className="comparison-label interpolated">Interpolated Frame</div>
      </div>
      <input
        className="comparison-slider"
        type="range"
        min="0"
        max="100"
        value={position}
        onChange={(event) => setPosition(Number(event.target.value))}
      />
    </section>
  );
}
