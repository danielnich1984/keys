import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import UserList from './components/UserList';
import InventoryAndOverview from './components/InventoryandOverview';
import KeyAssignment from './components/AssignKey';
import UserCreate from './components/UserCreate';

const AppRoutes = () => {
    return (
        <Router>
            <Routes>
                <Route path="/users" element={<UserList />} />``
                <Route path="/inventory" element={<InventoryAndOverview />} />
                <Route path="/assign" element={<KeyAssignment />} />
                <Route path="/newuser" element={<UserCreate />} />
            </Routes>
        </Router>
    );
};

export default AppRoutes;