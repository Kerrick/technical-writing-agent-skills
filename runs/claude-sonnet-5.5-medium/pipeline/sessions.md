# Sessions

Every headless session of this run, in order. Usage columns are the `usage` block of each `--output-format json` result (summed over the session's API calls); "context at end" is the last assistant message's input + cache tokens in the transcript, which is how full the context was when the session ended.

| Step | Session ID | Start | Model | input | cache_creation | cache_read | output | context at end | window | turns | time | status |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| 01-recall | `618b39d4-8c03-480b-9c56-d75e584f5bbb` | new | claude-sonnet-5-5 | 2 | 9719 | 11160 | 5 | 20881 | 1000000 | 1 | 2s | success |
| 02-baseline | `618b39d4-8c03-480b-9c56-d75e584f5bbb` | resume 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 8 | 52979 | 115048 | 13302 | 65485 | 1000000 | 15 | 123s | success |
| 03-reading-rails-1-list | `82772f61-b217-43ba-a646-493327473734` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 2 | 1186 | 65483 | 575 | 66671 | 1000000 | 2 | 12s | error_max_turns ERROR |
| 03-reading-rails-2-list | `ec6e45a7-538c-4488-9379-44eb621a7175` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 2 | 1196 | 65483 | 534 | 66681 | 1000000 | 2 | 16s | error_max_turns ERROR |
| 03-reading-rust-list | `468b8139-a365-4793-bc42-dea2d4479209` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 2 | 1135 | 65483 | 577 | 66620 | 1000000 | 2 | 22s | error_max_turns ERROR |
| 03-reading-postgres-list | `2b11aa9c-d024-45f3-8c2c-7588b6e50603` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 2 | 1300 | 65483 | 1293 | 66785 | 1000000 | 2 | 25s | error_max_turns ERROR |
| 03-reading-react-list | `b8a98614-9e6f-42bb-82be-eec4fd55ea96` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 2 | 1135 | 65483 | 525 | 66620 | 1000000 | 2 | 40s | error_max_turns ERROR |
| 03-reading-mdn-list | `a6694f7c-a925-4c5c-9ffd-7577df7cefb9` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 4 | 5544 | 66648 | 1666 | 72196 | 1000000 | 2 | 49s | error_max_turns ERROR |
| 03-reading-django-list | `f7e64911-385e-484c-9c6f-3daeb4f5990a` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 2 | 1374 | 65483 | 931 | 66859 | 1000000 | 2 | 51s | error_max_turns ERROR |
| 03-reading-ember-list | `444389bb-6f16-4461-b68f-62fa4cd48454` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 2 | 1144 | 65483 | 650 | 66629 | 1000000 | 2 | 60s | error_max_turns ERROR |
| 03-reading-mdn | `a6694f7c-a925-4c5c-9ffd-7577df7cefb9` | resume a6694f7c-a925-4c5c-9ffd-7577df7cefb9 | claude-sonnet-5-5 | 10 | 428388 | 957332 | 4566 | 500582 | 1000000 | 29 | 63s | success |
| 03-reading-rails-2 | `ec6e45a7-538c-4488-9379-44eb621a7175` | resume ec6e45a7-538c-4488-9379-44eb621a7175 | claude-sonnet-5-5 | 16 | 469335 | 2563848 | 5565 | 536016 | 1000000 | 32 | 71s | success |
| 03-reading-rails-1 | `82772f61-b217-43ba-a646-493327473734` | resume 82772f61-b217-43ba-a646-493327473734 | claude-sonnet-5-5 | 22 | 566213 | 4707723 | 6061 | 632884 | 1000000 | 32 | 96s | success |
| 03-reading-react | `b8a98614-9e6f-42bb-82be-eec4fd55ea96` | resume b8a98614-9e6f-42bb-82be-eec4fd55ea96 | claude-sonnet-5-5 | 20 | 676824 | 3479312 | 10005 | 743444 | 1000000 | 57 | 117s | success |
| 03-reading-django | `f7e64911-385e-484c-9c6f-3daeb4f5990a` | resume f7e64911-385e-484c-9c6f-3daeb4f5990a | claude-sonnet-5-5 | 32 | 471095 | 4362784 | 12897 | 537954 | 1000000 | 87 | 134s | success |
| 03-reading-rust | `468b8139-a365-4793-bc42-dea2d4479209` | resume 468b8139-a365-4793-bc42-dea2d4479209 | claude-sonnet-5-5 | 18 | 497464 | 1817644 | 15671 | 564084 | 1000000 | 112 | 143s | success |
| 03-reading-postgres | `2b11aa9c-d024-45f3-8c2c-7588b6e50603` | resume 2b11aa9c-d024-45f3-8c2c-7588b6e50603 | claude-sonnet-5-5 | 70 | 502452 | 11610396 | 8775 | 569237 | 1000000 | 37 | 165s | success |
| 03-reading-ember | `444389bb-6f16-4461-b68f-62fa4cd48454` | resume 444389bb-6f16-4461-b68f-62fa4cd48454 | claude-sonnet-5-5 | 14 | 421961 | 1401993 | 18828 | 488590 | 1000000 | 128 | 167s | success |
| 03-after-reading-postgres | `2b11aa9c-d024-45f3-8c2c-7588b6e50603` | resume 2b11aa9c-d024-45f3-8c2c-7588b6e50603 | claude-sonnet-5-5 | 26 | 145929 | 7629895 | 3402 | 715166 | 1000000 | 13 | 78s | success |
| 03-after-reading-mdn | `a6694f7c-a925-4c5c-9ffd-7577df7cefb9` | resume a6694f7c-a925-4c5c-9ffd-7577df7cefb9 | claude-sonnet-5-5 | 12 | 110238 | 2654427 | 6532 | 610820 | 1000000 | 40 | 79s | success |
| 04-compare-rails-1 | `82772f61-b217-43ba-a646-493327473734` | resume 82772f61-b217-43ba-a646-493327473734 | claude-sonnet-5-5 | 24 | 62294 | 7273713 | 34146 | 695178 | 1000000 | 24 | 281s | success |
| 04-compare-rails-2 | `ec6e45a7-538c-4488-9379-44eb621a7175` | resume ec6e45a7-538c-4488-9379-44eb621a7175 | claude-sonnet-5-5 | 14 | 59045 | 3380380 | 36904 | 595061 | 1000000 | 28 | 285s | success |
| 04-compare-react | `b8a98614-9e6f-42bb-82be-eec4fd55ea96` | resume b8a98614-9e6f-42bb-82be-eec4fd55ea96 | claude-sonnet-5-5 | 26 | 69219 | 9310138 | 46485 | 812663 | 1000000 | 32 | 395s | success |
| 04-compare-ember | `444389bb-6f16-4461-b68f-62fa4cd48454` | resume 444389bb-6f16-4461-b68f-62fa4cd48454 | claude-sonnet-5-5 | 28 | 83013 | 6838424 | 50129 | 571603 | 1000000 | 38 | 415s | success |
| 04-compare-rust | `468b8139-a365-4793-bc42-dea2d4479209` | resume 468b8139-a365-4793-bc42-dea2d4479209 | claude-sonnet-5-5 | 20 | 102524 | 5570772 | 55443 | 666608 | 1000000 | 27 | 432s | success |
| 04-compare-django | `f7e64911-385e-484c-9c6f-3daeb4f5990a` | resume f7e64911-385e-484c-9c6f-3daeb4f5990a | claude-sonnet-5-5 | 20 | 90130 | 5319446 | 54585 | 628084 | 1000000 | 38 | 447s | success |
| 04-compare-postgres | `2b11aa9c-d024-45f3-8c2c-7588b6e50603` | resume 2b11aa9c-d024-45f3-8c2c-7588b6e50603 | claude-sonnet-5-5 | 26 | 95586 | 9718860 | 56226 | 810752 | 1000000 | 40 | 438s | success |
| 04-compare-mdn | `a6694f7c-a925-4c5c-9ffd-7577df7cefb9` | resume a6694f7c-a925-4c5c-9ffd-7577df7cefb9 | claude-sonnet-5-5 | 18 | 198337 | 6508602 | 79152 | 809157 | 1000000 | 51 | 629s | success |
| 05-audit | `42a6c5db-ffa4-46a3-ba2b-5fa6ba88cfea` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 8 | 146164 | 479020 | 77672 | 211649 | 1000000 | 11 | 524s | success |
| 06-merge | `696ae08b-1814-40c6-986b-fcdccde9f3e3` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 6 | 108248 | 217130 | 90424 | 173733 | 1000000 | 3 | 611s | success |
| 07-check | `c6fa5f9d-2bea-4610-81c8-86023eb19c81` | fork of 618b39d4-8c03-480b-9c56-d75e584f5bbb | claude-sonnet-5-5 | 46 | 250696 | 4814763 | 89853 | 316181 | 1000000 | 99 | 695s | success |
| 08-apply | `696ae08b-1814-40c6-986b-fcdccde9f3e3` | resume 696ae08b-1814-40c6-986b-fcdccde9f3e3 | claude-sonnet-5-5 | 6 | 24370 | 524507 | 22933 | 198103 | 1000000 | 3 | 133s | success |
| 09-write | `55ab3a51-f15e-442f-a15b-6a448b4373ce` | new | claude-sonnet-5-5 | 16 | 62444 | 407075 | 13503 | 75168 | 1000000 | 19 | 88s | success |
| 09-write-fix | `55ab3a51-f15e-442f-a15b-6a448b4373ce` | resume 55ab3a51-f15e-442f-a15b-6a448b4373ce | claude-sonnet-5-5 | 4 | 5246 | 153439 | 776 | 80414 | 1000000 | 2 | 8s | success |
