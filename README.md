# pystable

Python wrapper for the [`libstable`](https://www.jstatsoft.org/article/view/v078i01) C library.

## Example

To fit with ML estimation:

```python
import pystable

alpha, beta, loc, scale = pystable.fit(data)
```

## Build `libstable`
### Dependencies
Install the GNU Scientific Library (GSL).

Arch Linux:
```
$ yay gsl
```

Mac:
```
$ brew install gsl
```

## Build `libstable`
```
$ cd libstable
$ make
```

or

```
$ poetry shell
$ poetry build
```



## TODO
- [ ] typings
- [ ] tests
- [ ] handle errors
  - [ ] handle NULL pointer errors
  - [ ] handle `err`
- [ ] create lib structure
- [x] create example file utilizing pystable lib
- [x] `import ctypes as ct`
