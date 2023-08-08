#include <cstdint>
#include <cstdlib>

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
    return 0;  // Values other than 0 and -1 are reserved for future use.
}
