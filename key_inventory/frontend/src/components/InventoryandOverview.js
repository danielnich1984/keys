import React from 'react';
import InventoryList from './Inventory';
import KeyOverview from './KeyOverview';

const InventoryAndOverview = () => {
  return (
    <div>
      <h1>Inventory and Keys Overview</h1>
      <KeyOverview />   {/* Displays the keys overview */}
      <br></br>
      <InventoryList />  {/* Displays the inventory list */}
    </div>
  );
};

export default InventoryAndOverview;