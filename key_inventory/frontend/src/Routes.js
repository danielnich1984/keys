import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import UserList from './components/UserList';
import InventoryAndOverview from './components/InventoryandOverview';

const AppRoutes = () => {
    return (
        <Router>
            <Routes>
                <Route path="/users" element={<UserList />} />``
                <Route path="/inventoryandoverview" element={<InventoryAndOverview />} />
            </Routes>
        </Router>
    );
};

export default AppRoutes;