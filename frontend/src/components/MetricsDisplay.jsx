export default function MetricsDisplay({ run }) {
  const metrics = run?.metrics;

  return (
    <section className="panel" id="metrics">
      <div className="panel-heading">
        <h3>Quality Metrics</h3>
        <span>Hackathon evaluation ready</span>
      </div>
      {!metrics ? (
        <p className="muted">Run interpolation to view SSIM, PSNR, and MSE.</p>
      ) : (
        <div className="metrics-grid">
          <div>
            <strong>{metrics.ssim}</strong>
            <p>SSIM</p>
          </div>
          <div>
            <strong>{metrics.psnr}</strong>
            <p>PSNR</p>
          </div>
          <div>
            <strong>{metrics.mse}</strong>
            <p>MSE</p>
          </div>
        </div>
      )}
    </section>
  );
}
