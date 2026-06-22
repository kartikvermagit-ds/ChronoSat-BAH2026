const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function parseJson(response) {
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    const detail = payload.detail || `API request failed with status ${response.status}`;
    throw new Error(detail);
  }
  return payload;
}

export function getArtifactUrl(filename) {
  return `${API_URL}/artifacts/${filename}`;
}

export async function uploadSatelliteFiles(files) {
  const formData = new FormData();
  files.forEach((file) => formData.append("files", file));
  const response = await fetch(`${API_URL}/upload`, {
    method: "POST",
    body: formData,
  });
  return parseJson(response);
}

export async function listUploadedFiles() {
  const response = await fetch(`${API_URL}/files`);
  return parseJson(response);
}

export async function startInterpolation(payload) {
  const response = await fetch(`${API_URL}/interpolate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return parseJson(response);
}

export async function listResults() {
  const response = await fetch(`${API_URL}/results`);
  return parseJson(response);
}
