import kue from 'kue';
import chai from 'chai';
import createPushNotificationsJobs from './8-job.js';

const { expect } = chai;

describe('createPushNotificationsJobs', function () {
  let queue;

  beforeEach(function () {
    // Create a new Kue queue in test mode
    queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1', db: 3 } });
    queue.testMode.enter();
  });

  afterEach(function (done) {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
    queue.testMode.exit();
    done();
  });

  it('should display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate that two jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);

    // Check job data and type
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('4153518780');
    expect(queue.testMode.jobs[0].data.message).to.equal('This is the code 1234 to verify your account');

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('4153518781');
    expect(queue.testMode.jobs[1].data.message).to.equal('This is the code 4562 to verify your account');
  });

});
