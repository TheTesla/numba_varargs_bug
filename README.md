# numba bug variadic parameter functions with additional parameters

## reproduce

```bash
python3 bug.py > bug.txt
python3 expected.py > expected.txt
diff bug.txt expected.txt
diff -u bug.txt expected.txt > diff.txt
```

## actual vs. expected output

```diff
--- bug.txt	2024-11-10 15:50:54.943184817 +0100
+++ expected.txt	2024-11-10 15:51:06.376460216 +0100
@@ -1,5 +1,5 @@
 
-actual results
+expected results
 f0(1.1,2.2,3.3,4.4,5.5,6.6):
   args[ 0 ] = 1.1
   args[ 1 ] = 2.2
@@ -8,31 +8,29 @@
   args[ 4 ] = 5.5
   args[ 5 ] = 6.6
 f1(1.1,2.2,3.3,4.4,5.5,6.6):
-  x = 2.2
-  args[ 0 ] = 1.1
-  args[ 1 ] = 2.2
-  args[ 2 ] = 3.3
-  args[ 3 ] = 4.4
-  args[ 4 ] = 5.5
+f1() missing 1 required keyword-only argument: 'x'
 f1(1.1,2.2,3.3,4.4,5.5,x=6.6):
-  x = 2.2
+  x = 6.6
   args[ 0 ] = 1.1
   args[ 1 ] = 2.2
   args[ 2 ] = 3.3
   args[ 3 ] = 4.4
+  args[ 4 ] = 5.5
 f2(1.1,2.2,3.3,4.4,5.5,6.6):
-  x = 2.2
+  x = 8.8
   args[ 0 ] = 1.1
   args[ 1 ] = 2.2
   args[ 2 ] = 3.3
   args[ 3 ] = 4.4
   args[ 4 ] = 5.5
+  args[ 5 ] = 6.6
 f2(1.1,2.2,3.3,4.4,5.5,x=6.6):
-  x = 2.2
+  x = 6.6
   args[ 0 ] = 1.1
   args[ 1 ] = 2.2
   args[ 2 ] = 3.3
   args[ 3 ] = 4.4
+  args[ 4 ] = 5.5
 f3(1.1,2.2,3.3,4.4,5.5,6.6):
   x = 1.1
   args[ 0 ] = 2.2
@@ -40,7 +38,7 @@
   args[ 2 ] = 4.4
   args[ 3 ] = 5.5
   args[ 4 ] = 6.6
-f4(1.1,2.2,3.3,4.4,5.5,6.6):
+f3(1.1,2.2,3.3,4.4,5.5,x=6.6):
   x = 1.1
   args[ 0 ] = 2.2
   args[ 1 ] = 3.3

```
