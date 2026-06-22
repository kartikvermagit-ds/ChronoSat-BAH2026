import logo from "../logo.png";

const stats = [
  { value: "12,500+", label: "Frames Processed" },
  { value: "91.4%", label: "Average SSIM" },
  { value: "3", label: "Satellite Sources" },
  { value: "15 Min", label: "Resolution" },
];

const badges = ["INSAT-3DS", "GOES-19", "Himawari-8"];

export default function Header() {
  return (
    <header className="hero">
      <div className="hero-copy-panel">
        <p className="eyebrow">Bharatiya Antariksh Hackathon 2026</p>
        <h1>ChronoSat</h1>
        <p className="hero-copy">
          Bridging temporal gaps in satellite imagery with optical flow, modular
          RIFE-ready interpolation, and evaluation metrics built for judges.
        </p>
        <div className="hero-actions">
          <a className="primary-button hero-button" href="#overview">
            Start Live Pipeline
          </a>
          <a className="secondary-button" href="#comparison">
            View Before vs After
          </a>
        </div>
        <div className="hero-badges">
          {badges.map((badge) => (
            <span key={badge} className="hero-badge">
              {badge}
            </span>
          ))}
        </div>
        <div className="hero-stats">
          {stats.map((stat) => (
            <article key={stat.label} className="stat-card">
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </article>
          ))}
        </div>
      </div>

      <div className="hero-visual" aria-hidden="true">
        <div className="space-orbit orbit-one" />
        <div className="space-orbit orbit-two" />
        <div className="space-orbit orbit-three" />
        <div className="orbit-dot dot-one" />
        <div className="orbit-dot dot-two" />
        <div className="orbit-dot dot-three" />
        <div className="planet-glow" />
        <div className="planet-earth">
          <div className="earth-cloud cloud-one" />
          <div className="earth-cloud cloud-two" />
          <div className="earth-cloud cloud-three" />
        </div>
        <div className="satellite-node">
          <div className="satellite-panel left" />
          <div className="satellite-body" />
          <div className="satellite-panel right" />
        </div>
        <img className="hero-logo floating-logo" src={logo} alt="ChronoSat mission logo" />
      </div>
    </header>
  );
}
