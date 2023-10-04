-- Current balance of each account
SELECT account_name, balance FROM Accounts WHERE user_id = 1;

-- Total expenses in each category for the current month
SELECT category, SUM(amount) as total_expenses FROM Transactions WHERE amount < 0 AND strftime('%Y-%m', transaction_date) = '2023-10' GROUP BY category;

-- Money left in the budget for each category
SELECT b.category, (b.amount + IFNULL(SUM(t.amount), 0)) as remaining_budget FROM Budgets b LEFT JOIN Transactions t ON b.category = t.category AND t.amount < 0 AND strftime('%Y-%m', t.transaction_date) = '2023-10' WHERE b.user_id = 1 GROUP BY b.category;
