import { createBrowserRouter } from 'react-router-dom';
import Layout from './Layout';
import Homepage from '../components/homepage';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Homepage />,
      }
    ],
  },
]);
