export function useMetrics(run) {
  if (!run?.quality) {
    return [];
  }

  return [
    { label: "MAE", value: run.quality.mae },
    { label: "Consistency", value: run.quality.temporal_consistency },
    { label: "Flow", value: run.quality.flow_magnitude },
  ];
}
