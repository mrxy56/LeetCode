/** 1. Promise.all() **/
/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    try {
        const [res1, res2] = await Promise.all([promise1, promise2]);
        return res1 + res2;
    } catch(error) {
        console.error(error);
        throw errow
    }
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */