import React, { useEffect, useState } from 'react';
import axios from 'axios';

const KeyOverview = () => {
  const [keys, setKeys] = useState([]);
  const [keyAssignments, setKeyAssignments] = useState([]);
  
  useEffect(() => {
    // Fetch key assignments data
    axios.get('http://localhost:8000/api/keyassignments/')
      .then(response => {
        setKeyAssignments(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the key assignments!", error);
      });

    // Fetch keys data (with quantities)
    axios.get('http://localhost:8000/api/keys/')
      .then(response => {
        setKeys(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the keys!", error);
      });
  }, []);

  const calculateStats = (key) => {
    // Calculate the statistics for each key
    const assignmentsForKey = keyAssignments.filter(assignment => assignment.key.id === key.id);

    const checkedOut = assignmentsForKey.filter(assignment => assignment.status === "CHECKED_OUT").length;
    const lost = assignmentsForKey.filter(assignment => assignment.status === "LOST").length;
    const totalQuantity = key.total_quantity;  // Use the total quantity from your backend
    const available = totalQuantity - checkedOut - lost;

    return { checkedOut, lost, available };
  };

  return (
    <div>
      <h1>Keys Overview</h1>
      <table>
        <thead>
          <tr>
            <th>Key Name</th>
            <th>Notes</th>
            <th>Total Quantity</th>
            <th>Checked Out</th>
            <th>Available</th>
            <th>Lost</th>
          </tr>
        </thead>
        <tbody>
          {keys.map((key) => {
            const { checkedOut, lost, available } = calculateStats(key);
            return (
              <tr key={key.id}>
                <td>{key.name}</td>
                <td>{key.notes}</td>
                <td>{key.total_quantity}</td>
                <td>{checkedOut}</td>
                <td>{available}</td>
                <td>{lost}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export default KeyOverview;
