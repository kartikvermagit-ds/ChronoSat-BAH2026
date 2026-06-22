export function getSatelliteSummary() {
  return [
    { name: "GOES-19", cadence: "10 min", coverage: "Americas" },
    { name: "INSAT-3DS", cadence: "15 min", coverage: "Indian Ocean Region" },
    { name: "Himawari-8", cadence: "10 min", coverage: "Asia-Pacific" },
  ];
}
