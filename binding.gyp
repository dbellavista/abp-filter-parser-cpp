{
  "targets": [{
    "target_name": "abp-filter-parser-cpp",
    "sources": [
      "addon.cpp",
      "ABPFilterParserWrap.cpp",
      "ABPFilterParserWrap.h",
      "ABPFilterParser.cpp",
      "ABPFilterParser.h",
      "cosmeticFilter.cpp",
      "cosmeticFilter.h",
      "filter.cpp",
      "filter.h",
      "<!(node -e "require(\'bloom-filter-cpp\'))/BloomFilter.cpp",
      "<!(node -e "require(\'bloom-filter-cpp\'))/BloomFilter.h",
      "<!(node -e "require(\'bloom-filter-cpp\'))/hashFn.cpp",
      "<!(node -e "require(\'bloom-filter-cpp\'))/hashFn.h",
      "<!(node -e "require(\'hashset-cpp-v10\'))/HashSet.cpp",
      "<!(node -e "require(\'hashset-cpp-v10\'))/HashSet.h"
    ],
    "include_dirs": [
      ".",
      "<!(node -e "require(\'bloom-filter-cpp\'))",
      "<!(node -e "require(\'hashset-cpp-v10\'))"
    ],
    "dependencies": [
    ],
    "conditions": [
      ['OS=="win"', {
        }, {
          'cflags_cc': [ '-fexceptions' ]
        }
      ]
    ],
    "xcode_settings": {
      "OTHER_CFLAGS": [ "-ObjC" ],
      "OTHER_CPLUSPLUSFLAGS" : ["-std=c++11","-stdlib=libc++", "-v"],
      "MACOSX_DEPLOYMENT_TARGET": "10.9",
      "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
    },
  }]
}
