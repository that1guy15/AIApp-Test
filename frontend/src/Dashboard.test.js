// Dashboard.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import { createMemoryHistory } from 'history';
import { Router } from 'react-router-dom';
import Dashboard from './Dashboard';

test('renders Dashboard with link to User List', () => {
  const history = createMemoryHistory();
  render(
    <Router history={history}>
      <Dashboard />
    </Router>
  );
  expect(screen.getByText(/Welcome to the Dashboard/i)).toBeInTheDocument();
  expect(screen.getByText(/Go to User List/i)).toBeInTheDocument();
});
