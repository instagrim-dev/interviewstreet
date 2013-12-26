# The authors of this work have released all rights to it and placed it
# in the public domain under the Creative Commons CC0 1.0 waiver
# (http://creativecommons.org/publicdomain/zero/1.0/).
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Retrieved from: http://en.literateprograms.org/Bucket_sort_(Python)?oldid=13661

def bucketSort(arr):
    count = [0] * len(arr)
    for value in arr:
        count[value] += 1
    arr = []
    for nr, amount in enumerate(count):
        arr.extend([nr] * amount)
    return arr


arr = [1,3,4,6,4,2,9,1,2,9]
arr2 = [11169221, 2545558, 8875250, 11986128, 0, 14123721, 13998827, 10754984]
arr3 = [6930886, -1692777, 4636915, 7747793, -4238335, 9885386, 9760492, 6516649]

for val in arr:
    print val,
print

arr = bucketSort(arr)

for val in arr:
    print val,
print
