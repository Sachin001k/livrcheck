-- LivrCheck: run this once in your Supabase project's SQL editor
-- (Dashboard -> SQL Editor -> New query -> paste -> Run).
--
-- Supabase Auth already provides the auth.users table used for login/signup
-- (auth.sign_up / auth.sign_in_with_password in auth.py). This adds the one
-- table LivrCheck needs to store each user's saved FIB-4 results, with Row
-- Level Security so a user can only ever read or write their own rows.

create table if not exists public.fib4_results (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references auth.users (id) not null,
    created_at timestamptz not null default now(),
    age integer not null,
    ast numeric not null,
    alt numeric not null,
    platelets numeric not null,
    score numeric not null,
    tier text not null
);

alter table public.fib4_results enable row level security;

create policy "Users can view their own results"
    on public.fib4_results for select
    using (auth.uid() = user_id);

create policy "Users can insert their own results"
    on public.fib4_results for insert
    with check (auth.uid() = user_id);
