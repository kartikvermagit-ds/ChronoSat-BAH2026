const defaultSteps = [
  "Reading .nc",
  "Extracting TIR1 Band",
  "Optical Flow",
  "RIFE Interpolation",
  "Metrics",
];

export default function ProcessingStatus({ status }) {
  const activeIndex =
    status.progressIndex ?? (status.state === "Completed" ? defaultSteps.length - 1 : -1);

  return (
    <section className="panel">
      <div className="panel-heading">
        <h3>Processing Status</h3>
        <span>{status.state}</span>
      </div>
      <p>{status.message}</p>
      <div className="progress-flow">
        {defaultSteps.map((step, index) => (
          <div key={step} className={`progress-step ${index <= activeIndex ? "active" : ""}`}>
            <span className="progress-dot" />
            <p>{step}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
