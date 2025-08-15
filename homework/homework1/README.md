# Budget Lens

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Young people these days often struggle with personal budgeting because they does not have clear visibility into where their money is going. While many banking apps show balances, they don't provide enough insight into spending categories or simple trends over time. This project aims to build a lightweight personal finance tracker that organizes expenses into categories and highlights monthly spending patterns. The goal is to help users make smarter decisions about saving and reduce unnecessary spending.

## Stakeholder & User

**Stakeholder:** The individual managing their personal budget.

**User:** The same person — checking the tracker regularly to see spending patterns.

**Workflow context:** Spending summaries should be available at the end of each week so users can adjust behavior quickly.

## Useful Answer & Decision

This project provides a descriptive weekly summary report, presented as a table and simple chart of spending by category, which helps the stakeholder identify where to cut costs and decide how much to save.

## Assumptions & Constraints

- Access to bank transaction data.
- Updates only once per week.
- Tooling limited to Python and Jupyter Notebook.
- Privacy: user's financial data stays local and is not shared.

## Known Unknowns / Risks

- Data may have unclear merchant names.
- Users may forget to upload transactions consistently.
- Risk that weekly summaries don't change behavior, which means may require adding goals or alerts later.

## Lifecycle Mapping

**Goal → Stage → Deliverable**

- Understand spending problem → Problem Framing & Scoping (Stage 01) → Scoping memo + repo setup
- Clean and categorize transactions → Stage 02 (Data & EDA) → Simple labeled dataset
- Produce weekly summary reports → Stage 03 (Modeling/Output) → Spending charts + table

## Repo Plan

- **`/data/`** → sample CSV of transactions
- **`/src/`** → scripts for cleaning and categorizing spending
- **`/notebooks/`** → exploratory notebook for analysis
- **`/docs/`** → memo + simple instructions

**Update cadence:** weekly commits and pushes
