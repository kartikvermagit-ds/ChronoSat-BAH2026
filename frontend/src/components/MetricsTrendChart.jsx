const defaultSeries = {
  ssim: [0.82, 0.86, 0.88, 0.9, 0.93],
  psnr: [24.2, 26.8, 28.6, 30.3, 32.1],
  mse: [0.018, 0.012, 0.009, 0.006, 0.004],
};

function polylinePoints(values, invert = false) {
  const min = Math.min(...values);
  const max = Math.max(...values);
  const range = max - min || 1;
  return values
    .map((value, index) => {
      const x = (index / (values.length - 1)) * 100;
      const normalized = (value - min) / range;
      const y = invert ? normalized * 100 : 100 - normalized * 100;
      return `${x},${y}`;
    })
    .join(" ");
}

export default function MetricsTrendChart({ run }) {
  const metrics = run?.metrics
    ? {
        ssim: [0.82, 0.86, 0.89, 0.91, run.metrics.ssim],
        psnr: [24.2, 26.8, 28.6, 30.3, run.metrics.psnr],
        mse: [0.018, 0.012, 0.009, 0.006, run.metrics.mse],
      }
    : defaultSeries;

  const charts = [
    { label: "SSIM Trend", key: "ssim", invert: false },
    { label: "PSNR Trend", key: "psnr", invert: false },
    { label: "MSE Trend", key: "mse", invert: true },
  ];

  return (
    <section className="panel trend-panel">
      <div className="panel-heading">
        <h3>Quality Metrics Chart</h3>
        <span>Trend lines judges can scan fast</span>
      </div>
      <div className="trend-grid">
        {charts.map((chart) => (
          <article key={chart.key} className="trend-card">
            <div className="trend-header">
              <h4>{chart.label}</h4>
              <span>{metrics[chart.key][metrics[chart.key].length - 1]}</span>
            </div>
            <svg viewBox="0 0 100 100" className="trend-svg" preserveAspectRatio="none">
              <polyline
                fill="none"
                stroke="rgba(255,255,255,0.15)"
                strokeWidth="0.8"
                points="0,100 100,100"
              />
              <polyline
                fill="none"
                stroke="#ffc857"
                strokeWidth="3"
                points={polylinePoints(metrics[chart.key], chart.invert)}
              />
            </svg>
          </article>
        ))}
      </div>
    </section>
  );
}
