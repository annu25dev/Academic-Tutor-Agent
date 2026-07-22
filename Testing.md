**RAG Pipeline Evaluation Report: Test 1 (RAGAS Faithfulness)**
First faithfulness run against the Academic Tutor RAG Agent. The point of this test is just to check the agent isn’t making things up - i.e. everything it says back should trace to something actually in the source docs, not filled in from the model’s own head.

##  Evaluation Overview
| Metric Evaluated | Faithfulness (via DeepEval) |
| Evaluation Model | `llama-3.3-70B` (via Groq API) |
| Target Threshold | `0.85` |
| Test Case Query | *"what is the primary topic of the uploaded study material?"* |
| Test Status | PASSED ✅ |
| Pass Rate | 100% (1/1 Tests Passed) |

RAG Pipeline Evaluation Report: Test 1 (Faithfulness)
First faithfulness run against the Academic Tutor RAG Agent. The point of this test is just to check the agent isn’t making things up - i.e. everything it says back should trace to something actually in the source docs, not filled in from the model’s own head.
Evaluation Overview

Terminal OUtput Summary

deepeval test run test_tutor.py
======================================================================

✓ Evaluation completed 🎉! (time taken: 31.76s | token cost: None)
» Test Results (1 total tests):
  » Pass Rate: 100.0% | Passed: 1 | Failed: 0
======================================================================

-----------------------------------------------------------------------------------------------------

**ROUTER ACCURACY TESTING REPORT: Test 2**

## Test Cases

|No.|               User Query              | Expected Agent | Selected Agent | Result |
| 1 | Explain Newton's laws in simple terms | Tutor          | Tutor          | ✅ Correct |
| 2 | Create a DBMS quiz                    | Quiz           | Quiz           | ✅ Correct |
| 3 | Make a study plan for semester exams  | Planner        | Planner        | ✅ Correct |
| 4 | Analyze my weak topics                | Assessment     | Assessment     | ✅ Correct |
| 5 | Explain recursion with examples       | Tutor          | Tutor          | ✅ Correct |
| 6 | Generate a Python quiz                | Quiz           | Quiz           | ✅ Correct |
| 7 | Create a revision timetable           | Planner        | Planner        | ✅ Correct |
| 8 | Explain uploaded notes topic          | Tutor          | Tutor          | ✅ Correct |
| 9 | Give feedback on my progress          | Assessment     | Assessment     | ✅ Correct |
| 10 | Explain Operating Systems concepts   | Tutor          | Tutor          | ✅ Correct |


## Router Accuracy Result

Total Test Cases: 10

Correct Routes: 10

Router Accuracy: 100%

-----------------------------------------------------------------------------------------------------

**RESPONSE LATENCY TESTING REPORT: Test 3**

## Test Run 1 

|No.| User Query                            | Response Latency |
| 1 | Explain Newton's laws in simple terms | 7.72 sec         |
| 2 | Create a DBMS quiz                    | 4.13 sec          |
| 3 | Make a study plan for semester exams  | 3.92 sec          |
| 4 | Analyze my weak topics                | 5.74 sec          |
| 5 | Explain recursion with examples       | 6.40 sec          |
| 6 | Generate a Python quiz                | 2.81 sec          |
| 7 | Create a revision timetable           | 5.23 sec          |
| 8 | Explain uploaded notes topic          | 3.55 sec          |
| 9 | Give feedback on my progress          | 7.09 sec          |
| 10 | Explain Operating Systems concepts   | 7.09 sec          |



## Final Response Latency Result

Total Test Cases: 10

Average Response Latency:

(7.72 + 4.13 + 3.92 + 5.74 + 6.40 + 2.81 + 5.23 + 3.55 + 7.09 + 7.09) / 10= 5.38 sec