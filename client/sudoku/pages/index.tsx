import React, { useEffect } from "react";

function Index() {
  const [message, setMessage] = React.useState("Loading...");
  useEffect(() => {
    fetch("http://localhost:8055/api/home")
      .then((response) => response.json())
      .then((data) => setMessage(data.message));
  }, []); // Added dependency array to prevent infinite loop
  return <div>{message}</div>;
}

export default Index;
