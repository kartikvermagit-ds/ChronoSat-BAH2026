import Footer from "../components/Footer";
import BeforeAfterDemo from "../components/BeforeAfterDemo";
import Dashboard from "../components/Dashboard";
import DataUpload from "../components/DataUpload";
import Header from "../components/Header";
import MetricsDisplay from "../components/MetricsDisplay";
import MetricsTrendChart from "../components/MetricsTrendChart";
import PipelineFlow from "../components/PipelineFlow";
import ProcessingStatus from "../components/ProcessingStatus";
import ResultsDashboard from "../components/ResultsDashboard";
import ResultsViewer from "../components/ResultsViewer";
import Sidebar from "../components/Sidebar";

export default function Home({
  run,
  satellite,
  onSatelliteChange,
  onRun,
  onUpload,
  onFilesChange,
  selectedFiles,
  uploadedFiles,
  status,
  isUploading,
  isInterpolating,
}) {
  return (
    <main className="layout">
      <Sidebar />
      <div className="content">
        <Header />
        <ResultsDashboard run={run} />
        <BeforeAfterDemo run={run} uploadedFiles={uploadedFiles} />
        <MetricsTrendChart run={run} />
        <PipelineFlow />
        <section className="grid">
          <DataUpload
            satellite={satellite}
            onSatelliteChange={onSatelliteChange}
            onRun={onRun}
            onUpload={onUpload}
            onFilesChange={onFilesChange}
            selectedFiles={selectedFiles}
            uploadedFiles={uploadedFiles}
            isUploading={isUploading}
            isInterpolating={isInterpolating}
          />
          <ProcessingStatus status={status} />
          <Dashboard run={run} />
          <MetricsDisplay run={run} />
          <ResultsViewer run={run} />
        </section>
        <Footer />
      </div>
    </main>
  );
}
