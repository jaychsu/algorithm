Complexity Analysis
======

## Case #1

- time: `O(N)`
- REF: https://en.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF

`N/2 + N/4 + N/8 + ... = N`

```java
int count = 0;
for (int i = N; i > 0; i /= 2) {
  for (int j = 0; j < i; j++) {
    count += 1;
  }
}
```

## Case #2

If X will always be a better choice for **large inputs**,
then we say that **an algorithm X is asymptotically more efficient than Y**.

## Case #3

- time: `O(N)`
- the `j` go through that array only once.

```java
int j = 0;
for(int i = 0; i < n; ++i) {
  while(j < n && arr[i] < arr[j]) {
    j++;
  }
}
```

## Case #4

- time: `O(2 ^ N)`
- REF: https://math.stackexchange.com/questions/177405/prove-by-induction-2n-cn-0-cn-1-cdots-cn-n

`C(n, 0) + C(n, 1) + ... + C(n, n) = 2 ^ n`
