import ResumeForm from "./components/ResumeForm";

function App() {
  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#1e1e1e",
        color: "#fff",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "900px",
          margin: "0 auto",
          padding: "40px 24px",
        }}
      >
        <h1 style={{ textAlign: "center" }}>AI Resume Screener</h1>
        <p style={{ textAlign: "center", opacity: 0.85 }}>
          Upload a resume and paste a job description to analyze match.
        </p>

        <ResumeForm />
      </div>
    </div>
  );
}

export default App;
