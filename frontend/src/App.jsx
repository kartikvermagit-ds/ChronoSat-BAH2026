import { useState } from "react";

import Home from "./pages/Home";
import "./styles/App.css";
import "./styles/components.css";
import "./styles/dashboard.css";
import { useProcessing } from "./hooks/useProcessing";

export default function App() {
  const [satellite, setSatellite] = useState("insat-3ds");
  const [selectedFiles, setSelectedFiles] = useState([]);
  const {
    run,
    uploadedFiles,
    status,
    isUploading,
    isInterpolating,
    triggerRun,
    uploadOnly,
  } = useProcessing();

  const handleFilesChange = (event) => {
    setSelectedFiles(Array.from(event.target.files || []));
  };

  return (
    <Home
      run={run}
      satellite={satellite}
      onSatelliteChange={setSatellite}
      onUpload={() => uploadOnly(selectedFiles)}
      onRun={() => triggerRun({ satellite, files: selectedFiles })}
      onFilesChange={handleFilesChange}
      selectedFiles={selectedFiles}
      uploadedFiles={uploadedFiles}
      status={status}
      isUploading={isUploading}
      isInterpolating={isInterpolating}
    />
  );
}
