import React from "react";

const Result = ({ recommendation }) => {
  return recommendation ? <h3>Recommended Diet: {recommendation}</h3> : null;
};

export default Result;
