import React, { useState } from "react";
import Form from "./components/Form";
import Result from "./components/Result";

function App() {
  const [recommendation, setRecommendation] = useState("");

  return (
    <div>
      <h1>Diet Recommendation System</h1>
      <Form setRecommendation={setRecommendation} />
      <Result recommendation={recommendation} />
    </div>
  );
}

export default App;
