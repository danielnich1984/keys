import React, { useState } from 'react';
import axios from 'axios';

const UserCreate = () => {
  const [userData, setUserData] = useState({
    fname: '',
    lname: '',
    email: '',
  });

  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserData({
      ...userData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Basic form validation
    if (!userData.fname || !userData.lname || !userData.email) {
      setError('All fields are required.');
      return;
    }

    // Send POST request to create user
    axios
      .post('http://localhost:8000/api/users/create/', userData)
      .then((response) => {
        console.log('User created:', response.data);
        // Optionally, redirect to another page after successful creation
        setError(null); // Clear error if any
      })
      .catch((error) => {
        console.error('Error creating user:', error.response || error);
        setError('An error occurred while creating the user.');
      });
  };

  return (
    <div>
      <h2>Create New User</h2>
      <form onSubmit={handleSubmit}>
        {error && <div style={{ color: 'red' }}>{error}</div>}
        <div>
          <label>First Name:</label>
          <input
            type="text"
            name="fname"
            value={userData.fname}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Last Name:</label>
          <input
            type="text"
            name="lname"
            value={userData.lname}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={userData.email}
            onChange={handleChange}
          />
        </div>
        <button type="submit">Create User</button>
      </form>
    </div>
  );
};

export default UserCreate;