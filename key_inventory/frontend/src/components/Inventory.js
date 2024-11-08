// frontend/src/components/UserList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';


const InventoryList = () => {
  const [inventory, setInventory] = useState([]);

  useEffect(() => {
    // Fetch data from the Django API endpoint
    axios.get('http://localhost:8000/api/keyassignments/')
    .then(response => {
      console.log(response.data);  // Log to ensure data is received correctly
      // Sort the inventory data by user.lname (last name)
      const sortedInventory = response.data.sort((a, b) => {
        const nameA = a.user?.lname?.toUpperCase() || '';  // Fallback to empty string if lname is missing
        const nameB = b.user?.lname?.toUpperCase() || '';  // Fallback to empty string if lname is missing
      
        if (nameA < nameB) return -1;
        if (nameA > nameB) return 1;
        return 0;
      });

        // Set state with the sorted data
        setInventory(sortedInventory);
      })
      .catch(error => {
        console.error("There was an error fetching the inventory data!", error);
      });
  }, []);

  return (
    <div>
      <h1>Inventory List</h1>
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Key Name</th>
            <th>Lost Key</th>
            <th>Status</th>
            
          </tr>
        </thead>
        <tbody>
          {inventory.map((assignment) => (
            <tr key={`${assignment.key.id}-${assignment.user.id}`}>
              <td>{assignment.user.fname}</td>
              <td>{assignment.user.lname}</td>
              <td>{assignment.status !== "LOST" ? assignment.key.name : ""}</td>
              <td>{assignment.status === "LOST" ? assignment.key.name : ""}</td>
              <td>{assignment.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};


export default InventoryList;