const links = [
  { label: "Overview", href: "#overview" },
  { label: "Pipeline", href: "#pipeline" },
  { label: "Metrics", href: "#metrics" },
  { label: "Docs", href: "#docs" },
];

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <div>
        <h2>Mission</h2>
        <p>Fill frame gaps between multi-satellite observations.</p>
      </div>
      <nav>
        {links.map((link) => (
          <a key={link.href} href={link.href}>
            {link.label}
          </a>
        ))}
      </nav>
    </aside>
  );
}
