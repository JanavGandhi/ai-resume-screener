import { useState } from "react";

function ResumeForm() {
  const [resume, setResume] = useState(null);
  const [jdText, setJdText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("jd_text", jdText);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/analyze-resume",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Server error");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Failed to analyze resume");
    } finally {
      setLoading(false);
    }
  };
return (
  <div
    style={{
      marginTop: "40px",
      padding: "24px",
      backgroundColor: "#2a2a2a",
      borderRadius: "8px",
    }}
  >
    <form onSubmit={handleSubmit}>
      <div>
        <label>Resume (PDF)</label><br />
        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setResume(e.target.files[0])}
          required
        />
      </div>

      <br />

      <div>
        <label>Job Description</label><br />
        <textarea
          rows="6"
          style={{ width: "100%" }}
          value={jdText}
          onChange={(e) => setJdText(e.target.value)}
          required
        />
      </div>

      <br />

      <button type="submit" disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>
    </form>

    <br />

    {error && <p style={{ color: "red" }}>{error}</p>}

    {result && (
      <div>
        <h2>Results</h2>
        <p><strong>TF-IDF Score:</strong> {result.tfidf_score}</p>
        <p><strong>BERT Score:</strong> {result.bert_score}</p>

        <h3>Common Skills</h3>
        <ul>
          {result.common_skills.map((skill, idx) => (
            <li key={idx}>{skill}</li>
          ))}
        </ul>

        <h3>Top Matching Sentences</h3>
        <ul>
          {result.top_sentences.map((item, idx) => (
            <li key={idx}>
              <em>{item.sentence}</em> (score: {item.score})
            </li>
          ))}
        </ul>
      </div>
    )}
  </div>
);

}

export default ResumeForm;
