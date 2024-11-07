// frontend/src/components/UserList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Fetch data from the Django API endpoint
    axios.get('http://localhost:8000/api/users/')
      .then(response => {
        setUsers(response.data);  // Set state with the fetched user data
      })
      .catch(error => {
        console.error("There was an error fetching the users!", error);
      });
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.fname} ({user.email})</li>  // Adjust to your fields
        ))}
      </ul>
    </div>
  );
};

export default UserList;