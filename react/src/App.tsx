import { useState, ChangeEvent, FormEvent } from 'react';

import { FormData } from './types';
import { initialFormData } from './types';
import "./App.css"


const App = () => {
  const [formData, setFormData] = useState<FormData>(initialFormData);
  const [prediction, setPrediction] = useState<string | null>(null);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
        const response = await fetch('http://localhost:8000/api/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setPrediction(data.prediction);
    } catch (error) {
        console.error('Error during fetch:', error);
    }
};

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div key={key}>
            <label>{key.replace(/_/g, ' ')}</label>
            <input
              type="text"
              name={key}
              value={formData[key as keyof FormData]}
              onChange={handleChange}
            />
          </div>
        ))}
        <button type="submit">Predict</button>
      </form>
      {prediction && (
        <div>
          <h3>Prediction: {prediction}</h3>
        </div>
      )}
    </div>
  );
}

export default App;