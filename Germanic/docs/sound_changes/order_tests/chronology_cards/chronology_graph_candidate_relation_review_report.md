# Chronology graph candidate relation review report

This report translates the card-level chronology audit into a relation-level review layer. Each ordinary card contributes up to two default boundary rows (earlier and later), and `SC031` / `SC033` contribute one additional supplementary expanded-PWGmc row each so that the present narrow integration policy remains explicit without replacing the default bundled-profile relations.

## Summary

1. **Relation rows created:** 142
2. **Counts by relation_kind:** broad_far_historical=18, local_historical=21, no_break_runner_boundary=23, one_sided_historical=5, reciprocal_historical=48, runner_limited=24, supplementary_expanded_profile=2, technical_marker=1
3. **Counts by graph_policy_bucket:** exclude_runner_boundary=47, exclude_technical_marker=1, include_contextual=23, include_core=69, supplementary_only=2

## Include-core relations

1. `SC016` before `SC017` (reciprocal_historical; support: SC016 later -> SC017; SC017 earlier -> SC016)
2. `SC017` before `SC019` (reciprocal_historical; support: SC017 later -> SC019; SC019 earlier -> SC017)
3. `SC019` before `SC020` (reciprocal_historical; support: SC019 later -> SC020; SC020 earlier -> SC019)
4. `SC020` before `SC042` (local_historical; support: SC042 earlier -> SC020)
5. `SC020` before `SC054` (local_historical; support: SC054 earlier -> SC020)
6. `SC026` before `SC027` (reciprocal_historical; support: SC026 later -> SC027; SC027 earlier -> SC026)
7. `SC029` before `SC030` (reciprocal_historical; support: SC029 later -> SC030; SC030 earlier -> SC029)
8. `SC030` before `SC032` (reciprocal_historical; support: SC030 later -> SC032; SC032 earlier -> SC030)
9. `SC031` before `SC034` (reciprocal_historical; support: SC031 later -> SC034; SC034 earlier -> SC031)
10. `SC032` before `SC040` (local_historical; support: SC032 later -> SC040)
11. `SC034` before `SC043` (local_historical; support: SC034 later -> SC043)
12. `SC034` before `SC047` (local_historical; support: SC047 earlier -> SC034)
13. `SC036` before `SC040` (local_historical; support: SC036 later -> SC040)
14. `SC039` before `SC040` (reciprocal_historical; support: SC039 later -> SC040; SC040 earlier -> SC039)
15. `SC041` before `SC046` (local_historical; support: SC041 later -> SC046)
16. `SC041` before `SC064` (local_historical; support: SC064 earlier -> SC041)
17. `SC042` before `SC043` (reciprocal_historical; support: SC042 later -> SC043; SC043 earlier -> SC042)
18. `SC043` before `SC044` (reciprocal_historical; support: SC043 later -> SC044; SC044 earlier -> SC043)
19. `SC043` before `SC046` (local_historical; support: SC046 earlier -> SC043)
20. `SC044` before `SC045` (reciprocal_historical; support: SC044 later -> SC045; SC045 earlier -> SC044)
21. `SC045` before `SC060` (local_historical; support: SC045 later -> SC060)
22. `SC046` before `SC048` (local_historical; support: SC046 later -> SC048)
23. `SC046` before `SC051` (local_historical; support: SC051 earlier -> SC046)
24. `SC048` before `SC059` (reciprocal_historical; support: SC048 later -> SC059; SC059 earlier -> SC048)
25. `SC050` before `SC052` (reciprocal_historical; support: SC050 later -> SC052; SC052 earlier -> SC050)
26. `SC051` before `SC056` (local_historical; support: SC051 later -> SC056)
27. `SC052` before `SC055` (reciprocal_historical; support: SC052 later -> SC055; SC055 earlier -> SC052)
28. `SC052` before `SC070` (local_historical; support: SC070 earlier -> SC052)
29. `SC054` before `SC063` (local_historical; support: SC054 later -> SC063)
30. `SC055` before `SC056` (reciprocal_historical; support: SC055 later -> SC056; SC056 earlier -> SC055)
31. `SC055` before `SC063` (local_historical; support: SC063 earlier -> SC055)
32. `SC055` before `SC066` (local_historical; support: SC066 earlier -> SC055)
33. `SC059` before `SC078` (local_historical; support: SC059 later -> SC078)
34. `SC063` before `SC072` (local_historical; support: SC063 later -> SC072)
35. `SC064` before `SC072` (reciprocal_historical; support: SC064 later -> SC072; SC072 earlier -> SC064)
36. `SC066` before `SC068` (reciprocal_historical; support: SC066 later -> SC068; SC068 earlier -> SC066)
37. `SC070` before `SC071` (reciprocal_historical; support: SC070 later -> SC071; SC071 earlier -> SC070)
38. `SC072` before `SC074` (local_historical; support: SC074 earlier -> SC072)
39. `SC073` before `SC085` (reciprocal_historical; support: SC073 later -> SC085; SC085 earlier -> SC073)
40. `SC074` before `SC075` (reciprocal_historical; support: SC074 later -> SC075; SC075 earlier -> SC074)
41. `SC078` before `SC086` (local_historical; support: SC078 later -> SC086)
42. `SC079` before `SC080` (reciprocal_historical; support: SC079 later -> SC080; SC080 earlier -> SC079)
43. `SC081` before `SC082` (reciprocal_historical; support: SC081 later -> SC082; SC082 earlier -> SC081)
44. `SC082` before `SC083` (reciprocal_historical; support: SC082 later -> SC083; SC083 earlier -> SC082)
45. `SC085` before `SC086` (reciprocal_historical; support: SC085 later -> SC086; SC086 earlier -> SC085)

## Include-contextual relations requiring policy judgement

1. `SC015` before `SC036` (broad_far_historical; support: SC015 later -> SC036)
2. `SC019` before `SC036` (broad_far_historical; support: SC036 earlier -> SC019)
3. `SC020` before `SC040` (broad_far_historical; support: SC020 later -> SC040)
4. `SC020` before `SC041` (broad_far_historical; support: SC041 earlier -> SC020)
5. `SC021` before `SC040` (broad_far_historical; support: SC021 later -> SC040)
6. `SC023` before `SC047` (broad_far_historical; support: SC023 later -> SC047)
7. `SC023` before `SC061` (one_sided_historical; support: SC061 earlier -> SC023)
8. `SC023` before `SC069` (broad_far_historical; support: SC069 earlier -> SC023)
9. `SC024` before `SC056` (broad_far_historical; support: SC024 later -> SC056)
10. `SC033` before `SC044` (broad_far_historical; support: SC033 later -> SC044)
11. `SC035` before `SC043` (one_sided_historical; support: SC035 later -> SC043)
12. `SC037` before `SC049` (one_sided_historical; support: SC049 earlier -> SC037)
13. `SC040` before `SC072` (broad_far_historical; support: SC040 later -> SC072)
14. `SC044` before `SC087` (broad_far_historical; support: SC087 earlier -> SC044)
15. `SC047` before `SC048` (broad_far_historical; support: SC047 later -> SC048; SC048 earlier -> SC047)
16. `SC052` before `SC057` (one_sided_historical; support: SC057 earlier -> SC052)
17. `SC055` before `SC060` (one_sided_historical; support: SC060 earlier -> SC055)
18. `SC055` before `SC079` (broad_far_historical; support: SC079 earlier -> SC055)
19. `SC055` before `SC081` (broad_far_historical; support: SC081 earlier -> SC055)
20. `SC070` before `SC078` (broad_far_historical; support: SC078 earlier -> SC070)
21. `SC072` before `SC073` (broad_far_historical; support: SC072 later -> SC073; SC073 earlier -> SC072)

## Excluded runner / no-break / technical / supplementary relations

1. `SC014` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
2. `SC014` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
3. `SC015` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
4. `SC016` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
5. `SC018` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
6. `SC018` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
7. `SC021` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
8. `SC022` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
9. `SC022` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
10. `SC023` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
11. `SC024` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
12. `SC025` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
13. `SC025` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
14. `SC026` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
15. `SC027` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
16. `SC028` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
17. `SC028` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
18. `SC029` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
19. `SC031` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
20. `SC033` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
21. `SC035` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
22. `SC037` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
23. `SC037` later -> `SC038` (technical_marker; exclude_technical_marker)
24. `SC039` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
25. `SC049` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
26. `SC050` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
27. `SC053` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
28. `SC053` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
29. `SC056` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
30. `SC057` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
31. `SC058` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
32. `SC058` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
33. `SC060` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
34. `SC061` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
35. `SC065` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
36. `SC065` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
37. `SC067` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
38. `SC067` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
39. `SC068` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
40. `SC069` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
41. `SC071` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
42. `SC075` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
43. `SC076` earlier -> `PWGmcChanges` (runner_limited; exclude_runner_boundary)
44. `SC076` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
45. `SC080` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
46. `SC083` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
47. `SC086` later -> `SC087` (no_break_runner_boundary; exclude_runner_boundary)
48. `SC087` later -> `runner_limit` (runner_limited; exclude_runner_boundary)
49. `SC031` expanded_pwgmc_note -> `SC011` (supplementary_expanded_profile; supplementary_only)
50. `SC033` expanded_pwgmc_note -> `SC008` (supplementary_expanded_profile; supplementary_only)

## Review / unclear relations

No review/unclear relations were identified in this pass.

## Card-level versus relation-level interpretation

There is no mechanical conflict with the card-level audit. The main difference is granularity:

1. the **33** card-level `graph_candidate=maybe` cases split into relation rows with buckets exclude_runner_boundary=27, exclude_technical_marker=1, include_contextual=18, include_core=20;
2. this means some card-level `maybe` files contain one historical relation that is usable only contextually while the opposite side is excluded as runner-limited/no-break evidence;
3. a smaller subset of `maybe` cards also contributes reciprocal or otherwise stronger historical relations once the earlier/later sides are separated.

So the relation review clarifies which individual boundaries are core candidates, which are contextual only, and which remain excluded, without changing the cards themselves.

## Recommendation

The next task should be a **graph/export policy draft**, not graph generation. That draft should define how `include_core`, `include_contextual`, `exclude_runner_boundary`, `exclude_technical_marker`, and `supplementary_only` relations should appear, if at all, in any later graph/export layer.

## Scope confirmation

This review layer is non-destructive: no chronology cards, default first-break TSVs, graph/export files, binaries, logs, or PDFs were edited or regenerated.
