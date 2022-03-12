**/cl.exe:
**/clang-cl.exe:
  invoke ${config_dir}/extractor.exe
  order compiler, extractor
  prepend --mimic
  prepend "${compiler}"
**/link.exe:
**/lld-link.exe:
  invoke ${config_dir}/extractor.exe
  order compiler, extractor
  prepend --ms-linker
  prepend --semmle-linker-executable
  prepend "${compiler}"
**/as.exe:
**/*-as.exe:
  invoke ${config_dir}/extractor.exe
  order compiler, extractor
  prepend --assembler
  prepend --codeql-assembler-executable
  prepend ${compiler}
**/collect2.exe:
  invoke ${config_dir}/extractor.exe
  order compiler, extractor
  prepend --linker
  prepend --semmle-linker-executable
  prepend "${compiler}"
**/ld*.exe:
**/*-ld*.exe:
  invoke ${config_dir}/extractor.exe
  order compiler, extractor
  prepend --linker
  prepend --semmle-linker-executable
  prepend "${compiler}"
**/*clang*.exe:
**/*cc*.exe:
**/*++*.exe:
**/c51.exe:
**/cx51.exe:
  invoke ${config_dir}/extractor.exe
  order compiler, extractor
  prepend --mimic
  prepend "${compiler}"
