# SQL-Injection-TEST

How SQL Injection works: An SQL query is sent to the website’s database. In the username field, my program appends an OR condition that always evaluates to true. Because of short-circuit evaluation, the server stops checking the rest of the query (such as the password). Since the OR condition is already true, the entire expression is considered true, and the password part is ignored. This results in a login being granted.

This technique is quite old. About ten years ago, it was very effective and allowed attackers to compromise many websites. Today, however, well‑secured sites use Prepared Statements, which prevent the query from being cut short. Even if an OR condition evaluates to true, the query is processed safely to the end.

About my program:

It only uses three harmless payloads.

The destructive payload (such as deleting users from the database) has been removed.

There may still be websites vulnerable to this technique, but my tool is intended only for testing.

I have tested it only on HackThisSite.org and on localhost.

Important Disclaimer: This program is not a hacking tool. It is designed solely to test whether a site is vulnerable to SQL Injection. Unauthorized use of this tool against real systems is illegal. If you attempt to hack with it, you are responsible for the consequences — not me. Misuse could lead to criminal prosecution.

<img width="800" height="600" alt="disclaimer" src="https://github.com/user-attachments/assets/438f26ab-a03e-40eb-9f44-9761bc9b855d" />

<img width="630" height="500" alt="screenshot" src="https://github.com/user-attachments/assets/079ac6df-8786-4e2a-9947-33e7428808a8" />

