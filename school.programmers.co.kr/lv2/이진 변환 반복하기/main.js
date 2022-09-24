/**
 * 이진 변환 함수
 * @param {string} s
 */
const to_binary = (s) => {
  /**
   *
   * @param {string} value
   * @returns
   */
  const _function = (value) => {
    /** @type { (s: string) => string }  */
    const get_rid_of_zeros = (s) => s.replace(/[0]/g, "");
    /** @type { (s: string) => number } */
    const to_length = (s) => s.length;
    /** @type { (s: number) => string } */
    const to_bin = (s) => s.toString(2);

    /** @type { (s: string) => string } */
    const all_in_once = (s) => to_bin(to_length(get_rid_of_zeros(s)));

    /** @type { (s: string) => number } */
    const count_zeros = (s) => s.match(/[0]/g)?.length || 0;

    return {
      value: () => value,
      convert: () => (value = all_in_once(value)),
      count_zeros: () => count_zeros(value),
    };
  };

  return _function(s);
};

/**
 * 솔루션 함수
 *
 * @param {string} s
 * @return {number[]}
 */
const solution = (s) => {
  let handler = to_binary(s);

  /**
   * 시도 횟수
   * @type {number}
   */
  let attempt = 0;

  /**
   * 제거된 0의 개수
   * @type {number}
   */
  let zeros = 0;

  while (handler.value() !== "1") {
    let before_zeros = handler.count_zeros(),
      after_zeros = 0;

    handler.convert();

    after_zeros = handler.count_zeros();

    zeros += before_zeros;
    attempt++;
  }

  return [attempt, zeros];
};
