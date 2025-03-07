// import logo from './logo.svg';
import React from 'react';
import './App.css';
import Product from './components/Product';

const App = () => {
  const products = [
    {
      id: "p1",
      title: "Nirma",
      amount: 100,
      date: new Date(2210, 8, 10)
    },
    {
      id: "p2",
      title: "Nirma",
      amount: 100,
      date: new Date(2210, 8, 10)
    },
    {
      id: "p3",
      title: "Nirma",
      amount: 100,
      date: new Date(2210, 8, 10)
    },
    {
      id: "p4",
      title: "Nirma",
      amount: 100,
      date: new Date(2210, 8, 10)
    }
  ];

  return (
    <div>
      {products.map(product => (
        <div key={product.id} className="card">
          <h2>{product.title}</h2>
          <p>Amount: ${product.amount}</p>
          <p>Date: {product.date.toDateString()}</p>
        </div>
      ))}
    </div>
  );
};

export default App;
