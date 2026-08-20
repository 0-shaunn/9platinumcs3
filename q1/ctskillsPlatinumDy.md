# Computational Thinking Exercise
## [Smart Vending Machine]
**Name:** Shaun Rodric B. Dy
**Section:** 9 - Platinum
**Last Name:** Dy
**Date:** August 20, 2026
---
## Step 1: Identify the Big Problem
### Main Problem
The current school vending machine system is inefficient and unreliable, leading to incorrect change distribution, unnotified stock depletion, user selection mistakes, and slow processing times during peak usage.
---
## Step 2: Identify the Sub-Problems
1. Incorrect Change Calculation
2. Lack of Inventory Tracking & Notification
3. User Selection & Interface Errors
4. Slow Transaction Processing Speed
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Incorrect Change Calculation | Algorithm Design | Create a step-by-step logic loop: ⁠Change = Cash_Inserted - Item_Price⁠. If ⁠Change > 0⁠, check available change reserve and dispense exact coins/bills before |
| Lack of Inventory Tracking & Notification | Pattern Recognition & Abstraction | Model stock counts digitally using variables for each item slot (e.g., ⁠item_A_count⁠). Decrease count by ⁠1⁠ per purchase, and trigger an automated notification to staff when ⁠item_count <= 2⁠. |
| User Selection & Interface Errors | Decomposition | Break the purchase process into distinct user steps: (1) Display item details & price, (2) Prompt user to press "Confirm", and (3) Allow a 5-second "Cancel" window before dispensing. |
| Slow Transaction Processing Speed | Algorithm Design & Abstraction | Streamline code by resetting payment and sensor loops immediately after item drop detection, eliminating unnecessary delayed processing functions between transactions. |
---
## Step 4: Algorithmic Solution
### Incorrect Change Calculation
Write the sub-problem you selected.
### Pseudocode
Here is the pseudocode focused specifically on Sub-Problem 1: Incorrect Change Calculation.
START CalculateChange
    INPUT item_price
    INPUT cash_inserted
 
    IF cash_inserted < item_price THEN
        DISPLAY "Insufficient funds. Please insert more money."
        RETURN cash_inserted
    ELSE
        change_due = cash_inserted - item_price

        IF change_due == 0 THEN
            DISPLAY "Exact amount received. No change required."
            DISPENSE item
        ELSE
            IF machine_change_reserve >= change_due THEN
                DISPENSE item
                DISPENSE change_due
                machine_change_reserve = machine_change_reserve - change_due
                DISPLAY "Transaction complete. Collect your item and change."
            ELSE
                DISPLAY "Error: Insufficient change in machine. Transaction canceled."
                RETURN cash_inserted
            ENDIF
        ENDIF
    ENDIF
END

