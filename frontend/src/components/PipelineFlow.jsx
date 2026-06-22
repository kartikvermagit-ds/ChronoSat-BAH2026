const steps = [
  { title: "Upload", description: "Satellite .nc / .h5 frames enter the pipeline." },
  { title: "Optical Flow", description: "Motion estimates align temporal changes." },
  { title: "RIFE", description: "Modular interpolation stage generates missing content." },
  { title: "Frame Generation", description: "Intermediate preview and final frame are saved." },
  { title: "Metrics", description: "SSIM, PSNR, and MSE are reported for evaluation." },
];

export default function PipelineFlow() {
  return (
    <section className="panel pipeline-panel">
      <div className="panel-heading">
        <h3>Live Pipeline Visualization</h3>
        <span>Realtime processing storyboard</span>
      </div>
      <div className="pipeline-steps">
        {steps.map((step, index) => (
          <article
            key={step.title}
            className="pipeline-step"
            style={{ animationDelay: `${index * 0.12}s` }}
          >
            <div className="step-index">{String(index + 1).padStart(2, "0")}</div>
            <div>
              <h4>{step.title}</h4>
              <p>{step.description}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
