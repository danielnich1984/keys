import React, { useState, useEffect } from 'react';

const KeyAssignment = () => {
  const [users, setUsers] = useState([]);
  const [keys, setKeys] = useState([]);
  const [selectedUser, setSelectedUser] = useState('');
  const [selectedKey, setSelectedKey] = useState('');

  // Fetch users for dropdown
  useEffect(() => {
    fetch('http://localhost:8000/api/users') // Adjust API endpoint as needed
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  // Fetch available keys for dropdown
  useEffect(() => {
    fetch('http://localhost:8000/api/keys') // Adjust API endpoint as needed
      .then(response => response.json())
      .then(data => setKeys(data))
      .catch(error => console.error('Error fetching keys:', error));
  }, []);

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();

    const data = { user_id: selectedUser, key_id: selectedKey };
    
    fetch('http://localhost:8000/api/assign-key', { // Adjust API endpoint as needed
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Key assigned:', data);
        alert('Key assigned successfully!');
      })
      .catch(error => {
        console.error('Error assigning key:', error);
        alert('Failed to assign key.');
      });
  };

  return (
    <div>
      <h2>Assign Key to User</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="user">Select User:</label>
          <select
            id="user"
            value={selectedUser}
            onChange={(e) => setSelectedUser(e.target.value)}
            required
          >
            <option value="">Select a user</option>
            {users.map(user => (
              <option key={user.id} value={user.id}>
                {user.fname} {user.lname} {/* Adjust based on user model */}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label htmlFor="key">Select Key:</label>
          <select
            id="key"
            value={selectedKey}
            onChange={(e) => setSelectedKey(e.target.value)}
            required
          >
            <option value="">Select a key</option>
            {keys.map(key => (
              <option key={key.id} value={key.id}>
                {key.name} {/* Adjust based on key model */}
              </option>
            ))}
          </select>
        </div>

        <button type="submit">Assign Key</button>
      </form>
    </div>
  );
};

export default KeyAssignment;