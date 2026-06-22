import { useState } from "react";

import {
  executeProcessingFlow,
  fetchUploadedFiles,
  runInterpolationOnly,
  uploadFilesOnly,
} from "../services/processingService";

export function useProcessing() {
  const [run, setRun] = useState(null);
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [isUploading, setIsUploading] = useState(false);
  const [isInterpolating, setIsInterpolating] = useState(false);
  const [status, setStatus] = useState({
    state: "Idle",
    message: "Choose satellite files, upload them, and launch interpolation.",
    progressIndex: -1,
  });

  const refreshFiles = async () => {
    const response = await fetchUploadedFiles();
    setUploadedFiles(response.files);
  };

  const uploadOnly = async (files) => {
    setIsUploading(true);
    setStatus({
      state: "Uploading",
      message: "Uploading satellite files...",
      progressIndex: 0,
    });

    try {
      const result = await uploadFilesOnly(files);
      setUploadedFiles(result.files);
      setStatus({
        state: "Uploaded",
        message: `${result.files.length} file(s) uploaded successfully.`,
        progressIndex: 0,
      });
    } catch (error) {
      setStatus({
        state: "Failed",
        message: error.message,
        progressIndex: -1,
      });
    } finally {
      setIsUploading(false);
    }
  };

  const triggerRun = async ({ satellite, files }) => {
    setIsInterpolating(true);
    setStatus({
      state: "Running",
      message: `Reading files for ${satellite}...`,
      progressIndex: 0,
    });

    try {
      await new Promise((resolve) => setTimeout(resolve, 220));
      setStatus({
        state: "Running",
        message: "Extracting TIR1 Band...",
        progressIndex: 1,
      });

      await new Promise((resolve) => setTimeout(resolve, 220));
      setStatus({
        state: "Running",
        message: "Computing optical flow...",
        progressIndex: 2,
      });

      await new Promise((resolve) => setTimeout(resolve, 220));
      setStatus({
        state: "Running",
        message: "Applying RIFE interpolation...",
        progressIndex: 3,
      });

      const result = await executeProcessingFlow({ files, satellite });
      setRun(result.run);
      setUploadedFiles(result.upload.files);
      setStatus({
        state: "Completed",
        message: `Metrics generated and interpolation completed for ${satellite}.`,
        progressIndex: 4,
      });
    } catch (error) {
      setStatus({
        state: "Failed",
        message: error.message,
        progressIndex: -1,
      });
    } finally {
      setIsInterpolating(false);
    }
  };

  return {
    run,
    uploadedFiles,
    status,
    isUploading,
    isInterpolating,
    isRunning: isUploading || isInterpolating,
    triggerRun,
    uploadOnly,
    refreshFiles,
  };
}
