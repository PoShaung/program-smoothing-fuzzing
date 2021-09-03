# program-smoothing-fuzzing

## Environment

Tested on Linux verison 4.15.0-76-generic Ubuntu 18.04 64bit with RTX 2080ti

- Python 3.7
- Pytorch 1.3.1

## Setup

### Execution of the baseline fuzzers

For the execution procedures of the baseline fuzzers, please refer to the following links:

- [AFL](https://github.com/google/AFL)
- [Neuzz](https://github.com/Dongdongshe/neuzz)
- [MTFuzz](https://github.com/rahlk/MTFuzz)


### Fuzzing with the RESuzz

> The procedures are the same to the neuzz variants.
```shell

# build the fuzzer
$ gcc -O3 -funroll-loops ./fuzz.c -o fuzz

# start fuzz (max_len refers to the maximum size of the inital seeds)
$ python nn.py /path/to/program [params]
$ ./fuzz -i fuzz_input -o seeds -l max_len /path/to/program [params] @@

```


## Benchmark Statistics

### SE:

1. [ICSE-2020] Ankou: Guiding Grey-box Fuzzing towards Combinatorial Difference
2. [ASE-2020] Zeror: Speed Up Fuzzing with Coverage-sensitive Tracing and Scheduling
3. [FSE-2020] CrFuzz: Fuzzing Multi-purpose Programs through Input Validation
4. [ICSE-2020] Typestate-Guided Fuzzer for Discovering Use-after-Free Vulnerabilities (short for TGFDV)
6. [ISSTA-2020] WEIZZ: Automatic Grey-Box Fuzzing for Structured Binary Formats

### Security:

7. [NDSS-2020] Not All Coverage Measurements Are Equal:ßFuzzing by Coverage Accounting for Input (short for NCME)
9. [S&P-2020] IJON: Exploring Deep State Spaces via Fuzzing
10. [S&P-2020] PANGOLIN: Incremental Hybrid Fuzzing with Polyhedral Path Abstraction
11. [S&P-2020] RetroWrite: Statically Instrumenting COTS Binaries for Fuzzing and Sanitization
12. [USENIX-2020] GREYONE: Data Flow Sensitive Fuzzing

<!-- ### Else

13. [FSE-2017] Steelix: Program-State Based Binary Fuzzing
14. [CCS-2019] Matryoshka: Fuzzing Deeply Nested Branches
15. [S&P 2018] Angora: Efﬁcient Fuzzing by Principled Search
16. [ICSE-2020] MemLock: Memory Usage Guided Fuzzing
17. [USENIX-2020] ParmeSan: Sanitizer-guided Greybox Fuzzing -->


### Summarize
<!-- 

| Extended Benchmark                                | Paper                                                        |
| ------------------------------------------------- | ------------------------------------------------------------ |
| tcpdump                                           | Ankou[1], WEIZZ[6], PANGOLIN[10], RetroWrite[11], Steelix[13], Matryoshka[14] |
| jhead                                             | PANGOLIN[10], Matryoshka[14], Angora[15]                     |
| xmlwf                                             | Matryoshka[14], Angora[15]                                   |
| bison                                             | Ankou[1], GREYONE[12]                                        |
| libtiff (tiff2pdf tiff2ps tiffdump tiffinfo)      | Ankou[1], CrFuzz[3], NCME[7],  IJON[9],  PANGOLIN[10], Steelix[13] |
| libpng (pngimage pngfix pngtest)                  | Zeror[2], WEIZZ[6], PANGOLIN[10], ParmeSan[17]               |
| libming(listaction Listaction_d)                  | Ankou[1], NCME[7], MemLock[16]                               | -->



| Extended Benchmark                           | ICSE-2020     | ASE-2020 | FSE-2020 | ISSTA-2020 | NDSS-2020 | USENIX-2020 | S&P-2020 |
| -------------------------------------------- | ------------- | -------- | -------- | ---------- | --------- | ----------- | -------- |
| tcpdump                                      | Ankou         |          |          | WEIZZ      |           |             | PANGOLIN RetroWrite|
| jhead                                        |               |          |          |            |           |             | PANGOLIN |
| bison                                        | Ankou         |          |          |            |           |             |          |
| libtiff (tiff2pdf tiff2ps tiffdump tiffinfo) | Ankou         |          | CrFuzz   |            | NCME      |             |          |
| libpng (pngimage pngfix pngtest)             |               | Zeror    |          | WEIZZ      |           | ParmeSan    | PANGOLIN |
| libming(listaction Listaction_d)             | Ankou MemLock |          |          |            | NCME      |             |          |
| nasm                                         | Ankou         |          |          |            | NCME      | GREYONE     |          |
| libsass                                      | Ankou  TGFDV  |          |          |            |           | GREYONE     |          |
| xmlwf                                        | Ankou         |          | CrFuzz   |            | NCME      |             |          |
| base64                                       |               |          |          |            | NCME      | GREYONE     | PANGOLIN    RetroWrite|
| md5sum                                       |               |          |          |            | NCME      | GREYONE     |  PANGOLIN   RetroWrite|
| uniq                                         |               |          |          |            | NCME      | GREYONE     | PANGOLIN    RetroWrite|
| who                                          |               |          |          |            | NCME      | GREYONE     |  PANGOLIN   RetroWrite|



