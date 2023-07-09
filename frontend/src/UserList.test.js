// UserList.test.js
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom/extend-expect';
import axios from 'axios';
import { createMemoryHistory } from 'history';
import { Router } from 'react-router-dom';
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import UserList from './UserList';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json([
      { _id: '1', name: 'User 1', email: 'user1@example.com', age: 30, color: 'red' },
      { _id: '2', name: 'User 2', email: 'user2@example.com', age: 31, color: 'blue' }
    ]));
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test('fetches users and renders them on mount', async () => {
  const history = createMemoryHistory();
  render(
    <Router history={history}>
      <UserList />
    </Router>
  );
  const items = await waitFor(() => screen.getAllByRole('listitem'));
  expect(items).toHaveLength(2);
});

test('filters users based on input', async () => {
  const history = createMemoryHistory();
  render(
    <Router history={history}>
      <UserList />
    </Router>
  );
  await waitFor(() => screen.getByRole('listitem'));
  userEvent.type(screen.getByPlaceholderText(/Filter users/i), 'User 1');
  expect(screen.getByText(/User 1/)).toBeInTheDocument();
  expect(screen.queryByText(/User 2/)).not.toBeInTheDocument();
});
